import React from "react";
import Cell from "./Cell";

function Board(){

    return <div className="board">
            <div className="column">
                <Cell id={"0"} />
                <Cell id={"1"} />
                <Cell id={"2"} />
                <Cell id={"3"} />
                <Cell id={"4"} />
                <Cell id={"5"} />
            </div>
            <div className="column">
                <Cell id={"6"} />
                <Cell id={"7"} />
                <Cell id={"8"} />
                <Cell id={"9"} />
                <Cell id={"10"} />
                <Cell id={"11"} />
            </div>
            <div className="column">
                <Cell id={"12"} />
                <Cell id={"13"} />
                <Cell id={"14"} />
                <Cell id={"15"} />
                <Cell id={"16"} />
                <Cell id={"17"} />
            </div>
            <div className="column">
                <Cell id={"18"} />
                <Cell id={"19"} />
                <Cell id={"20"} />
                <Cell id={"21"} />
                <Cell id={"22"} />
                <Cell id={"23"} />
            </div>
            <div className="column">
                <Cell id={"24"} />
                <Cell id={"25"} />
                <Cell id={"26"} />
                <Cell id={"27"} />
                <Cell id={"28"} />
                <Cell id={"29"} />
            </div>
            <div className="column">
                <Cell id={"30"} />
                <Cell id={"31"} />
                <Cell id={"32"} />
                <Cell id={"33"} />
                <Cell id={"34"} />
                <Cell id={"35"} />
            </div>
                
        </div>
}

export default Board;