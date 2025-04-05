package com.example.demo.controllers;

import com.example.demo.services.LogService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/logs")
public class LogController {

    private LogService logService;

    public LogController(LogService logService) {
        this.logService = logService;
    }

    @GetMapping("/limit/{number}")
    public List<String> limitLogs(@PathVariable("number") int number) throws IOException {
        List<String> result = this.logService.limitLogs(number);
        return result;
    }

    @GetMapping("/offset/{number}")
    public List<String> offsetLogs(@PathVariable("number") int number) throws IOException {
        List<String> result = this.logService.limitLogs(number);
        return result;
    }

    @GetMapping("/sort/date/{type}")
    public List<String> sortLogsByDate(@PathVariable("type") String type) throws IOException
    {
        List<String> result = this.logService.sortLogsByDate(type);
        return result;
    }

    @GetMapping("/sort/time/{type}")
    public List<String> sortLogsByTime(@PathVariable("type") String type) throws IOException
    {
        List<String> result = this.logService.sortLogsByTime(type);
        return result;
    }

    @GetMapping("/filter/{type}")
    public List<String> filterLogs(@PathVariable("type") String type) throws IOException
    {
        List<String> result = this.logService.filterLogs(type);
        return result;
    }

    @GetMapping("/search/{text}")
    public List<String> searchLogs(@PathVariable("text") String text) throws IOException
    {
        List<String> result = this.logService.searchLogs(text);
        return result;
    }

    @GetMapping("/datetime/{start}")
    public List<String> datetimeFromLogs(@PathVariable("start") LocalDateTime start) throws IOException
    {
        List<String> result = this.logService.datetimeFromLogs(start);
        return result;
    }

    @GetMapping("/datetime/{start}/{end}")
    public List<String> datetimeFromToLogs(@PathVariable("start") LocalDateTime start, @PathVariable("end") LocalDateTime end) throws IOException
    {
        List<String> result = this.logService.datetimeFromToLogs(start, end);
        return result;
    }

}
