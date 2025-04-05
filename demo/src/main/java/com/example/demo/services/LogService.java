package com.example.demo.services;

import com.example.demo.repositories.LogRepository;

import java.io.IOException;
import java.time.LocalDateTime;
import java.util.List;

public class LogService {
    private LogRepository logRepository;

    public LogService(LogRepository logRepository)
    {
        this.logRepository = logRepository;
    }

    public List<String> limitLogs(int number) throws IOException {
        List<String> result = this.logRepository.limitLogs(number);
        return result;
    }

    public List<String> offsetLogs(int number) throws IOException
    {
        List<String> result = this.logRepository.offsetLogs(number);
        return result;
    }

    public List<String> sortLogsByDate(String type) throws IOException
    {
        List<String> result = this.logRepository.sortLogsByDate(type);
        return result;
    }

    public List<String> sortLogsByTime(String type) throws IOException
    {
        List<String> result = this.logRepository.sortLogsByTime(type);
        return result;
    }

    public List<String> filterLogs(String type) throws IOException {
        List<String> result = this.logRepository.filterLogs(type);
        return result;
    }

    public List<String> searchLogs(String text) throws IOException {
        List<String> result = this.logRepository.searchLogs(text);
        return result;
    }


    public List<String> datetimeFromLogs(LocalDateTime start) throws IOException {
        List<String> result = this.logRepository.datetimeFromLogs(start);
        return result;
    }

    public List<String> datetimeFromToLogs(LocalDateTime start, LocalDateTime end) throws IOException {
        List<String> result = this.logRepository.datetimeFromToLogs(start, end);
        return result;
    }
}
