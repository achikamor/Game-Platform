import React from "react";
import FileUP from "./FilesUP";
import Difficulty from "./Difficulty";

function Submission(){
    return <form className="criteria">
        <FileUP />
        <Difficulty />
    </form>
}

export default Submission;