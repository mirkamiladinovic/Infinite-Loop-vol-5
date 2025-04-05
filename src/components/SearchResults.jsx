import React from "react";
import styles from "../styles/SearchResults.module.css";
import axios from "axios";
const SearchResults = ({
    itemLimitProp,
    logTypeProp,
    setSelectedLogTypeProp,
}) => {
    const tableHeaders = ["time", "type", "service", "filename", "details"];

    const logLines = [
        "[2025-03-10 05:46:58.958] DEBUG garage-servicing-api EchoChamber.Security.OrderService.cs: Invalid credentials provided for Unknown. The provided username or password does not match our records. Failed login attempt: user19@example.com",
        "[2025-03-10 18:20:03.958] INFO garage-experience-api Oblivion.Helpers.FileUploader.cs: Failed to parse response from b40e8cce-5327-45ce-9a08-b0b5ef272f2b. The response format from the server was not valid. Please check server-side logging for user13@example.com.",
        "[2025-03-10 05:46:58.958] DEBUG garage-servicing-api EchoChamber.Security.OrderService.cs: Invalid credentials provided for Unknown. The provided username or password does not match our records. Failed login attempt: user19@example.com",
        "[2025-03-10 18:20:03.958] ERROR garage-experience-api Oblivion.Helpers.FileUploader.cs: Failed to parse response from b40e8cce-5327-45ce-9a08-b0b5ef272f2b. The response format from the server was not valid. Please check server-side logging for user13@example.com.",
        "[2025-03-10 05:46:58.958] WARNING garage-servicing-api EchoChamber.Security.OrderService.cs: Invalid credentials provided for Unknown. The provided username or password does not match our records. Failed login attempt: user19@example.com",
        "[2025-03-10 18:20:03.958] INFO garage-experience-api Oblivion.Helpers.FileUploader.cs: Failed to parse response from b40e8cce-5327-45ce-9a08-b0b5ef272f2b. The response format from the server was not valid. Please check server-side logging for user13@example.com.",
        "[2025-03-10 05:46:58.958] DEBUG garage-servicing-api EchoChamber.Security.OrderService.cs: Invalid credentials provided for Unknown. The provided username or password does not match our records. Failed login attempt: user19@example.com",
        "[2025-03-10 18:20:03.958] INFO garage-experience-api Oblivion.Helpers.FileUploader.cs: Failed to parse response from b40e8cce-5327-45ce-9a08-b0b5ef272f2b. The response format from the server was not valid. Please check server-side logging for user13@example.com.",
        "[2025-03-10 05:46:58.958] DEBUG garage-servicing-api EchoChamber.Security.OrderService.cs: Invalid credentials provided for Unknown. The provided username or password does not match our records. Failed login attempt: user19@example.com",
        "[2025-03-10 18:20:03.958] INFO garage-experience-api Oblivion.Helpers.FileUploader.cs: Failed to parse response from b40e8cce-5327-45ce-9a08-b0b5ef272f2b. The response format from the server was not valid. Please check server-side logging for user13@example.com.",
        "[2025-03-10 05:46:58.958] DEBUG garage-servicing-api EchoChamber.Security.OrderService.cs: Invalid credentials provided for Unknown. The provided username or password does not match our records. Failed login attempt: user19@example.com",
        "[2025-03-10 18:20:03.958] INFO garage-experience-api Oblivion.Helpers.FileUploader.cs: Failed to parse response from b40e8cce-5327-45ce-9a08-b0b5ef272f2b. The response format from the server was not valid. Please check server-side logging for user13@example.com.",
        "[2025-03-10 05:46:58.958] DEBUG garage-servicing-api EchoChamber.Security.OrderService.cs: Invalid credentials provided for Unknown. The provided username or password does not match our records. Failed login attempt: user19@example.com",
        "[2025-03-10 18:20:03.958] INFO garage-experience-api Oblivion.Helpers.FileUploader.cs: Failed to parse response from b40e8cce-5327-45ce-9a08-b0b5ef272f2b. The response format from the server was not valid. Please check server-side logging for user13@example.com.",
    ];

    const parseLine = (line) => {
        const splitLine = line.split(" ", 5);
        const tmp = splitLine.join(" ");
        const details = line.slice(tmp.length + 1);
        console.log(splitLine);
        console.log(details);
        const datetime =
            splitLine[0].substring(1) +
            " " +
            splitLine[1].substring(0, splitLine[1].length - 1);
        console.log(datetime);
        const type = splitLine[2];
        const service = splitLine[3];
        const filename = splitLine[4];

        return { datetime, type, service, filename, details };
    };

    const makePages = () => {
        const pageSize = itemLimitProp;
        const pages = Math.ceil(logLines.length / pageSize);

        return Array.from({ length: pages }, (_, index) => index + 1);
    };

    return (
        <div className={styles.container}>
            <table className={styles.searchResultsTable}>
                <thead>
                    <tr>
                        {tableHeaders.map((header, index) => (
                            <th key={index} className={styles[header]}>
                                {header}
                            </th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {logLines.map((line, index) => (
                        <tr key={index}>
                            {Object.values(parseLine(line)).map(
                                (value, index) => (
                                    <td
                                        key={index}
                                        className={`${
                                            styles[
                                                index % 2 === 0 ? "even" : "odd"
                                            ]
                                        } ${styles[value]}`}
                                    >
                                        {value}
                                    </td>
                                )
                            )}
                        </tr>
                    ))}
                </tbody>
            </table>

            <div className={styles.paginationDiv}>
                {makePages().map((index) => (
                    <button key={index} onClick={() => console.log(index)}>
                        {index}
                    </button>
                ))}
            </div>
        </div>
    );
};

export default SearchResults;
