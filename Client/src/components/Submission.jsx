import React from "react";
import FileUP from "./FilesUP";
import Difficulty from "./Difficulty";
import ReactDOM from "react-dom";
import App from "./App";

function Submission(){

    async function handleClick(){
        alert("submited");
        const response = await fetch("http://localhost:5000/game");
        const moves = response.moves;
        // var matrix1 = [[1,2,0,0,0,0],
        //         [0,0,4,4,0,0],
        //         [0,0,0,0,0,0],
        //         [4,4,0,0,0,4],
        //         [0,0,0,0,0,0],
        //         [5,4,4,4,0,0]];
        // var matrix2 = [[0,0,0,0,0,0],
        //         [1,2,4,4,0,0],
        //         [0,0,0,0,0,0],
        //         [4,4,0,0,0,4],
        //         [0,0,0,0,0,0],
        //         [5,4,4,4,0,0]];
        // var matrix3 = [[0,0,0,0,0,0],
        //     [3,0,4,4,0,0],
        //     [1,2,0,0,0,0],
        //     [4,4,0,0,0,4],
        //     [0,0,0,0,0,0],
        //     [5,4,4,4,0,0]]
        // var matrix4 = [[0,0,0,0,0,0],
        //     [3,0,4,4,0,0],
        //     [0,1,2,0,0,0],
        //     [4,4,0,0,0,4],
        //     [0,0,0,0,0,0],
        //     [5,4,4,4,0,0]]
        // var moves = [[matrix1, false, false, "running"], [matrix2, false, false, "running"], [matrix3, false, true, "running"], [matrix4, false, false, "running"]]

        ReactDOM.render(<App data={moves} />, document.getElementById("root"));

    }

// check the action url!!   also goto package.jason and in line 14 I added the 'set PORT' to run react on localhost5000
    return <form className="criteria" id="form" action="http://localhost:5000" method="POST" >  
        <FileUP />
        <Difficulty />
        <button type="submit" className="submit_button" onClick={handleClick} >Submit</button>
    </form>
}

export default Submission;