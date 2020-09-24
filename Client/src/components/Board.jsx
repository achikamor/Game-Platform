import React from "react";
import Square from "./Square";

function Board(){
    return <div>
        {/* <h1 className="whosPlaying">Next player is : X</h1> */}
        <div className="board">
            <div className="board-row" style={{marginTop: "5px"}}>
                <Square src={null} id={"sq0"} />
                <Square src={null} id={"sq1"} />
                <Square src={null} id={"sq2"} />
            </div>
            <div className="board-row">
                <Square src={null} id={"sq3"} />
                <Square src={null} id={"sq4"}/>
                <Square src={null} id={"sq5"} />
            </div>
            <div className="board-row">
                <Square src={null} id={"sq6"} />
                <Square src={null} id={"sq7"} />
                <Square src={null} id={"sq8"} />
            </div>
       

        </div>
    </div> 
    
}

export default Board;