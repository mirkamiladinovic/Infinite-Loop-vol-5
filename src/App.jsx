import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import SearchTools from "./components/SearchTools";
import "./App.css";
import SearchResults from "./components/SearchResults";

function App() {
    const [count, setCount] = useState(0);
    const [itemLimit, setItemLimit] = useState(10);
    const [logType, setSelectedLogType] = useState("INFO");

    return (
        <div className="container">
            <SearchTools
                itemLimitProp={itemLimit}
                setItemLimitProp={setItemLimit}
                logTypeProp={logType}
                setSelectedLogTypeProp={setSelectedLogType}
            />
            <SearchResults
                itemLimitProp={itemLimit}
                setItemLimitProp={setItemLimit}
                logTypeProp={logType}
                setSelectedLogTypeProp={setSelectedLogType}
            />
        </div>
    );
}

export default App;
