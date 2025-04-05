const fs = require('fs');
const readline = require('readline');

var logs = {
    error: 0,
    debug: 0,
    info:  0,
    warning:0
}

var filesWithErrors = {}

async function processLineByLine() {
  const fileStream = fs.createReadStream('vegini_logovi.txt');

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });
  // Note: we use the crlfDelay option to recognize all instances of CR LF
  // ('\r\n') in input.txt as a single line break.

  var k = 0;
  for await (const line of rl) {
    // Each line in input.txt will be successively available here as `line`.
    //console.log(`${line}`);
    

    var path = (line.split(' ')[4]);
    path = path.slice(0,path.length-1);

    var fileName = path.split('.');
    fileName = fileName[fileName.length-2] + ".cs"; 


    if(line.indexOf("WARNING")>-1){
        logs.warning++;
    } else if(line.indexOf("DEBUG")>-1){
        logs.debug++;
    } else if(line.indexOf("ERROR")>-1){
        if(filesWithErrors[fileName] == undefined){
            filesWithErrors[fileName] = 1
        } else {
            filesWithErrors[fileName]++;
        } 
        logs.error++;

        fs.appendFile("./errors.txt", line + "\n", err =>{
            if(err) {
                console.log(err);
            }
        })
    } else if(line.indexOf("INFO")>-1){
        logs.info++;
    }
  }
  var sortable = []
  for(const file in filesWithErrors){
    sortable.push([file, filesWithErrors[file]]);
  }
  sortable.sort((a,b) =>{
    return b[1] - a[1];
  })
  sortable = sortable.slice(0,5);


  console.log(logs);
  console.log(sortable);
}

processLineByLine();



const express = require('express')
const app = express()
const port = 3000

app.get('/search', async (req, res) => {
    const fileStream = fs.createReadStream('vegini_logovi.txt');

  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  var k = 0;
  var temp = [];
  for await (const line of rl) {
    //Filtri
    if(req.query.logType != undefined){
        if(line.indexOf(req.query.logType) <= -1){
            continue;
        }
    }
    if(req.query.text != undefined){
        if(line.indexOf(req.query.text) <= -1){
            continue;
        }
    }
    //Filter vremenskog intervala nije zavrsen
    if(req.query.timeInterval != undefined){
        var firstBound = req.query.timeInterval.split("]-[")[0] ;
        var secondBound = req.query.timeInterval.split("]-[")[1];
        var target = line.split(" ")[0] + " " + line.split(" ")[1] ;
        
        firstBound = firstBound.slice(1, firstBound.length);
        secondBound = secondBound.slice(0, secondBound.length -1);
        target = target.slice(1,target.length-1);
        
        //console.log(firstBound);
        //console.log(secondBound);
        //console.log(target)
        //break;
    }

    temp.push(line);
    //Sortiranje
    if(req.query.sort != undefined){
        temp = temp.sort((a,b) => {
            var a = line.split(" ")[0] + " " + line.split(" ")[1] ;
            a=a.replace(" ", "T");
            a=a.slice(1,a.length-1);
            dateA = new Date(a);
    
            var b = line.split(" ")[0] + " " + line.split(" ")[1] ;
            b=b.replace(" ", "T");
            b=b.slice(1,b.length-1);
            dateB = new Date(b);
    
            return dateA.getTime() - dateB.getTime();
        })
    }

    k++;
    if(k == Number(req.query.limit[1])){
        break;
    }
  }
  res.send(temp)
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})