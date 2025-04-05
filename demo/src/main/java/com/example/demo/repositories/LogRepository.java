package com.example.demo.repositories;

import org.springframework.web.bind.annotation.PathVariable;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class LogRepository {
    public List<String> limitLogs(int number) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("../veginilogovi.txt"));
        List<String> result = new ArrayList<>();
        String log = bufferedReader.readLine();
        for(int i = 0; i < number; i++)
        {
            if (log != null)
                result.add(log);
            log = bufferedReader.readLine();
        }

        return result;
    }

    public List<String> offsetLogs(int number) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new FileReader("../veginilogovi.txt"));
        List<String> result = new ArrayList<>();
        String log = bufferedReader.readLine();
        for(int i = 0; i < number - 1; i++)
        {
            if(log != null)
                log = bufferedReader.readLine();
        }

        log = bufferedReader.readLine();

        while (log != null)
        {
            result.add(log);
            log = bufferedReader.readLine();
        }

        return result;
    }

    public List<String> sortLogsByDate(String type) throws IOException
    {
        List<String> result = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(new FileReader("../veginilogovi.txt"));

        String log = bufferedReader.readLine();
        result.add(log);



        return result;
    }

    public List<String> sortLogsByTime(@PathVariable("type") String type) throws IOException
    {
        List<String> result = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(new FileReader("../veginilogovi.txt"));

        String log = bufferedReader.readLine();
        result.add(log);

        return result;
    }

    public List<String> filterLogs(@PathVariable("type") String type) throws IOException
    {
        List<String> result = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(new FileReader("../veginilogovi.txt"));

        String log = bufferedReader.readLine();

        while(log != null)
        {
            if (log.contains(type.toUpperCase()))
            {
                result.add(log);
            }
            log = bufferedReader.readLine();
        }

        return result;
    }

    public List<String> searchLogs(@PathVariable("text") String text) throws IOException
    {
        List<String> result = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(new FileReader("../veginilogovi.txt"));

        String log = bufferedReader.readLine();

        while(log != null)
        {
            if (log.contains(text.toUpperCase()) || log.contains(text.toLowerCase()))
            {
                result.add(log);
            }

            log = bufferedReader.readLine();
        }

        return result;
    }

    public List<String> datetimeFromLogs(@PathVariable("start") LocalDateTime start) throws IOException
    {
        List<String> result = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(new FileReader("../veginilogovi.txt"));

        String log = bufferedReader.readLine();

        while(log != null)
        {
            int year = Integer.parseInt(log.substring(1, 5));
            int month = Integer.parseInt(log.substring(6, 8));
            int day = Integer.parseInt(log.substring(9, 11));
            int hour = Integer.parseInt(log.substring(12, 14));
            int minute = Integer.parseInt(log.substring(15, 17));
            int second = Integer.parseInt(log.substring(18, 20));

            LocalDateTime localDateTime = LocalDateTime.of(year, month, day, hour, minute, second);

            if (localDateTime.isAfter(start))
            {
                result.add(log);
            }

            log = bufferedReader.readLine();
        }

        return result;
    }

    public List<String> datetimeFromToLogs(@PathVariable("start") LocalDateTime start, @PathVariable("end") LocalDateTime end) throws IOException
    {
        List<String> result = new ArrayList<>();
        BufferedReader bufferedReader = new BufferedReader(new FileReader("../veginilogovi.txt"));

        String log = bufferedReader.readLine();

        while(log != null)
        {
            int year = Integer.parseInt(log.substring(1, 5));
            int month = Integer.parseInt(log.substring(6, 8));
            int day = Integer.parseInt(log.substring(9, 11));
            int hour = Integer.parseInt(log.substring(12, 14));
            int minute = Integer.parseInt(log.substring(15, 17));
            int second = Integer.parseInt(log.substring(18, 20));

            LocalDateTime localDateTime = LocalDateTime.of(year, month, day, hour, minute, second);

            if (localDateTime.isAfter(start) && localDateTime.isBefore(end))
            {
                result.add(log);
            }

            log = bufferedReader.readLine();
        }

        return result;
    }
}
