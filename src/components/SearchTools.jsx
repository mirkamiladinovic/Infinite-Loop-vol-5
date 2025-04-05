import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import styles from "../styles/SearchTools.module.css";
import { useState } from "react";
const logType = ["INFO", "DEBUG", "WARNING", "ERROR"];

const SearchTools = ({
    itemLimitProp,
    setItemLimitProp,
    logTypeProp,
    setSelectedLogTypeProp,
}) => {
    const [selectedLogType, setSelectedLogType] = useState("INFO"); // info je defaultno selektovan
    const [searchText, setSearchText] = useState("");
    const [itemLimit, setItemLimit] = useState(10);
    const itemLimits = [10, 20, 30];

    return (
        <div className={styles.container}>
            <div className={styles.dropDownDiv}>
                <select
                    className={styles.dropDown}
                    onChange={(e) => {
                        setSelectedLogType(e.target.value);
                        setSelectedLogTypeProp(e.target.value);
                    }}
                >
                    {logType.map((type, index) => (
                        <option
                            key={index}
                            value={type}
                            className={`${styles[type]}`}
                        >
                            {type}
                        </option>
                    ))}
                </select>
            </div>

            <div className={styles.itemLimitsDiv}>
                <select
                    className={styles.LimitsMenu}
                    onChange={(e) => {
                        setItemLimit(e.target.value);
                        console.log(e.target.value);
                        setItemLimitProp(e.target.value);
                    }}
                >
                    {itemLimits.map((item, index) => (
                        <option key={index} value={item}>
                            {item}
                        </option>
                    ))}
                </select>
            </div>

            <div className={styles.searchBarDiv}>
                <input
                    type="text"
                    placeholder="Search"
                    className={styles.searchBar}
                    onInput={(e) => {
                        setSearchText(e.target.value);
                        console.log(e.target.value);
                    }}
                />
                <FontAwesomeIcon
                    icon={faSearch}
                    className={styles.searchIcon}
                />
            </div>
            <div className={styles.dateTimePickerDiv}>
                <input
                    type="datetime-local"
                    className={styles.dateTimePicker}
                />
                <span> - </span>
                <input
                    type="datetime-local"
                    className={styles.dateTimePicker}
                    onChange={(e) => {
                        console.log(e.target.value);
                    }}
                />
            </div>
        </div>
    );
};

export default SearchTools;
