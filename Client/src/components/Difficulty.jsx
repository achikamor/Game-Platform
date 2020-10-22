import React from "react";
// import ReactDOM from "react-dom";
// import App from "./App";

function Difficulty(){

    // async function handleClick(){
    //     // const response = await fetch("www.nitzanim.co.il/gameresult");
    //     // const moves = response.moves;
    //     var matrix1 = [[1,2,0,0,0,0],
    //             [0,0,4,4,0,0],
    //             [0,0,0,0,0,0],
    //             [4,4,0,0,0,4],
    //             [0,0,0,0,0,0],
    //             [5,4,4,4,0,0]];
    //     var matrix2 = [[0,0,0,0,0,0],
    //             [1,2,4,4,0,0],
    //             [0,0,0,0,0,0],
    //             [4,4,0,0,0,4],
    //             [0,0,0,0,0,0],
    //             [5,4,4,4,0,0]];
    //     var matrix3 = [[0,0,0,0,0,0],
    //         [3,0,4,4,0,0],
    //         [1,2,0,0,0,0],
    //         [4,4,0,0,0,4],
    //         [0,0,0,0,0,0],
    //         [5,4,4,4,0,0]]
    //     var matrix4 = [[0,0,0,0,0,0],
    //         [3,0,4,4,0,0],
    //         [0,1,2,0,0,0],
    //         [4,4,0,0,0,4],
    //         [0,0,0,0,0,0],
    //         [5,4,4,4,0,0]]
    //     var moves = [[matrix1, false, false, "running"], [matrix2, false, false, "running"], [matrix3, false, true, "running"], [matrix4, false, false, "running"]]

    //     ReactDOM.render(<App data={moves} />, document.getElementById("root"));
    // }
    return <div>
        <div className="board_diff">
            <h3>Choose Board difficulty</h3>
            <input type="checkbox" id="board_diff1" name="board_diff1" value="1" />
            <label htmlFor="board_diff1"> 1</label><br/>
            <input type="checkbox" id="board_diff2" name="board_diff2" value="2" />
            <label htmlFor="board_diff2"> 2</label><br/>
            <input type="checkbox" id="board_diff3" name="board_diff3" value="3" />
            <label htmlFor="board_diff3"> 3</label><br/>
            <input type="checkbox" id="board_diff4" name="board_diff3" value="4" />
            <label htmlFor="board_diff4"> 4</label><br/>
            <input type="checkbox" id="board_diff5" name="board_diff3" value="5" />
            <label htmlFor="board_diff5"> 5</label><br/>

        </div>

        <div className="algo_diff">
            <h3>Choose Computer difficulty</h3>
            <input type="checkbox" id="computer_diff1" name="computer_diff1" value="1" />
            <label htmlFor="computer_diff1"> empty player</label><br/>
            <input type="checkbox" id="computer_diff2" name="computer_diff2" value="2" />
            <label htmlFor="computer_diff2"> level 1</label><br/>
            <input type="checkbox" id="board_diff3" name="computer_diff3" value="3" />
            <label htmlFor="computer_diff3"> level 2</label><br/>
            <input type="checkbox" id="board_diff4" name="computer_diff3" value="4" />
            <label htmlFor="computer_diff4"> level 3</label><br/>
            <input type="checkbox" id="computer_diff5" name="computer_diff3" value="5" />
            <label htmlFor="computer_diff5"> level 4</label><br/>
        </div>

        
    </div>
}

export default Difficulty;