import React from "react";
import ReactDOM from "react-dom";
import Header from "./Header";
import Footer from "./Footer";
import Submission from "./Submission";
import Board from "./Board";
import Wall from "./Wall";
import Door from "./Door";
import Player1 from "./Player1";
import Player2 from "./Player2";
import Bomb from "./Bomb";

function App(){
    
    
    const sleep = (milisec) => {return new Promise(resolve => setTimeout(resolve, milisec))}

    async function play(){
        var matrix1 = [[1,2,0,0,0,0],
                [0,0,4,4,0,0],
                [0,0,0,0,0,0],
                [4,4,0,0,0,4],
                [0,0,0,0,0,0],
                [5,4,4,4,0,0]];
        var matrix2 = [[0,0,0,0,0,0],
                [1,2,4,4,0,0],
                [0,0,0,0,0,0],
                [4,4,0,0,0,4],
                [0,0,0,0,0,0],
                [5,4,4,4,0,0]];
        var matrix3 = [[0,0,0,0,0,0],
            [3,0,4,4,0,0],
            [1,2,0,0,0,0],
            [4,4,0,0,0,4],
            [0,0,0,0,0,0],
            [5,4,4,4,0,0]]
        var matrix4 = [[0,0,0,0,0,0],
            [3,0,4,4,0,0],
            [0,1,2,0,0,0],
            [4,4,0,0,0,4],
            [0,0,0,0,0,0],
            [5,4,4,4,0,0]]
        var moves = [[matrix1, false, false, NaN], [matrix2, false, false, NaN], [matrix3, false, false, NaN], [matrix4, false, false, NaN]] 

        for(var i=0; i<moves.length; i++){
            var move = moves[i];
            var world = move[0];
            // var isStuck1 = move[1];
            // var isStuck2 = move[2];
            // var winner = move[3];
            for(var col=0; col<world.length; col++){
                for(var row=0; row<world[col].length; row++){
                    var location = col*world.length + row;
                    var to_render = <div/>;
                    if(world[col][row] === 1)
                        to_render = <Player1 />;
                    else if(world[col][row] === 2)
                        to_render = <Player2 />
                    else if(world[col][row] === 3)
                        to_render = <Bomb />
                    else if(world[col][row] === 4)
                        to_render = <Wall />
                    else if(world[col][row] === 5)
                        to_render = <Door />

                    ReactDOM.render(to_render, document.getElementById(location.toString()));

                }
            }
            
            await sleep(2000);
        }
        // ReactDOM.render(<Wall />, document.getElementById("8"));
        // ReactDOM.render(<Wall />, document.getElementById("18"));
        // ReactDOM.render(<Wall />, document.getElementById("2"));
    }
    
    return <div>
        <Header />
        <Submission />
        <Board />
        <button type="submit" className="button" onClick={play}>Play Game</button>
        <Footer />
    </div>
}

export default App;