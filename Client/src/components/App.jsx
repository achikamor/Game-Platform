import React, { useState } from "react";
import ReactDOM from "react-dom";
import Header from "./Header";
import Footer from "./Footer";
import Board from "./Board";
import Wall from "./Wall";
import Door from "./Door";
import Player1 from "./Player1";
import Player2 from "./Player2";
import Bomb from "./Bomb";

function App(props){
    const [isRunning, setRunning] = useState(false);
    const [isStop, setStop] = useState(false);
    const [runner, setRunner] = useState(0);
    var moves = props.data;
    


    const sleep = (milisec) => {return new Promise(resolve => setTimeout(resolve, milisec))}

    async function play(moves){
        if(!isRunning){
            setRunning(true);   
            for(var i=runner; i<moves.length; i++){
                while(isStop){
                    await sleep(1000);
                }
                
                var move = moves[i];
                var world = move[0];
                var game_state = move[3];
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
                ReactDOM.render(<h2>{game_state}</h2>, document.getElementById("game_state"));
                // var noMove = "";
                // if(move[1])
                //     noMove += "playe1 is stuck";
                // if(move[2])
                //     noMove +="player2 is stuck";
                // ReactDOM.render(<h3>{noMove}</h3>,document.getElementById("movemnt"));
                setRunner(runner + 1);
                await sleep(2000);
            }
            setRunner(0);
            setRunning(false);
            setStop(false);

        }


    }

    function stop_game(){
        if(isRunning){
            alert("press OK to continue");
            setStop(true);
        }
    }

    
    return <div>
        <Header />
        <Board />
        <button type="submit" className="Start" onClick={function(){play(moves)}}>Play Game</button>
        <button type="submit" className="Stop" onClick={stop_game}>Stop</button>
        <Footer />
    </div>
}

export default App;