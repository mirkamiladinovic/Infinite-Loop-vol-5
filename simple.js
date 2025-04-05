import fs from 'fs/promises';
import readline from 'readline';

import { exit, stdin as input, stdout as output } from 'node:process';

const rl = readline.createInterface({ input, output });

async function main() {
    let logs = [];
    let counts = {
        error: 0,
        warn: 0,
        info: 0,
        debug: 0,
    };
    let errors = [];

    let map = new Map();

    while(true) {
        console.log("Available options:")
        console.log("  0) Exit")
        console.log("  1) Load file")
        console.log("  2) Show breakdown by type")
        console.log("  3) Show problematic files")
        console.log("  4) Generate Errors file")
        const res = await new Promise((resolve) => {
            rl.question("Select an option (type the number): ", (answ) => resolve(answ));
        });
        if(res === "1") {
            const res = await new Promise((res) => {
                rl.question("Please put file path: ", (answ) => res(answ));
            });
            const data = (await fs.readFile(res)).toString();
            logs = [];
            errors = [];
            counts = {
                error: 0,
                warn: 0,
                info: 0,
                debug: 0,
            };
            map = new Map();

            for(const line of data.split("\n")) {
                if(line.length === 0) continue;
                const time = line.substring(1, 24);
                const [type, service, fileTmp, ...rest] = line.substring(26).split(" ");
                const file = fileTmp.substring(0, fileTmp.length - 1);
                const message = rest.join(" ").trim();

                const log = {time, type, service, file, message};
                logs.push(log)
                // console.log(log);

                if(type === "ERROR") {
                    counts.error += 1;
                    map.set(file, (map.get(file) ?? 1) + 1);
                    errors.push(line);
                } else if(type === "WARNING") {
                    counts.warn += 1;
                } else if(type === "INFO") {
                    counts.info += 1;
                } else if(type === "DEBUG") {
                    counts.debug += 1;
                }
            }
        } else if(res === "2") {
            console.log("There is:")
            console.log(`  ${counts.error} Errors`);
            console.log(`  ${counts.warn} Warnings`);
            console.log(`  ${counts.info} Infos`);
            console.log(`  ${counts.debug} Debugs`);
        } else if(res === "0") {
            exit(0)
        } else if(res === "3") {
            const res = await new Promise((res) => {
                rl.question("Max number of files: ", (answ) => res(answ));
            });
            const files = Array.from(map.entries()).sort(([_, count]) => count);
            console.log("Files with most errors:")
            for(let i = 0; i < parseInt(res) && i < files.length;i++) {
                console.log(`  - ${files[i][0]} with ${files[i][1]} errors`);
            }
        } else if(res === "4") {
            const res = await new Promise((res) => {
                rl.question("Output file path: ", (answ) => res(answ));
            });
            await fs.writeFile(res, errors.join("\n"));
        } else if(res === "0") {
            exit(0)
        } else {
            console.log("Unknown command!");
        }
    }
}

main().catch(err => console.error(err));
