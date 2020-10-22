import React from "react";

function GameButtons(){
    return <div>
            <button type="submit" className="button" onClick="return false;" >Stop</button>
            <button className="button" onClick="return false;" >Play next move</button>
            <button type="submit" className="button" onClick="return false;" >Play Game</button>
    </div>
}

export default GameButtons;