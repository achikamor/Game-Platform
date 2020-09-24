import React, {useState} from "react";
import Header from "./Header";
import Footer from "./Footer";
// import Note from "./Note";
import Board from "./Board";



function App(){

    const sleep = (milisec) => {return new Promise(resolve => setTimeout(resolve, milisec))}

    const [board, setBoard] = useState(<Board />);  
    // var moveNumber = 0;
    async function play(){
        var moves = [{player:"X", position: "0"}, {player:"O", position: "3"}, {player:"X", position: "4"}, {player:"O", position: "5"}, {player:"X", position: "8"}]
        // moves.forEach(newMove => { 
        //     setBoard(document.getElementById("sq"+newMove.position).innerHTML = newMove.player)
        // });

        // moves.map((move) => setBoard(document.getElementById("sq"+move.position).innerHTML = move.player));
        for(var i=0; i<moves.length; i++){
            setBoard(document.getElementById("sq"+moves[i].position).innerHTML = moves[i].player);
            await sleep(1000);
        }
            
        
        // if (moveNumber < moves.length){
        //     var currMove = moves[moveNumber];
        //     setBoard(document.getElementById("sq"+currMove.position).innerHTML = currMove.player);
        //     moveNumber ++;
            // var image = document.createElement("img");
            // currMove.player === 1? image.src = "../public/axe.png" : image.src = "../public/circ.png";
            // setBoard(ReactDOM.render(board, document.getElementById("sq"+currMove.position).src = currMove.player === 1 ? "../../public/axe.png"  : "../../public/circ.png"));
        //}
    }
        
        

    return <div>
        <Header />
        {/* <h1 className="whosPlaying">next player is: {prop.player}</h1> */}
        <Board />
        <button onClick={play} className="button">Play next move</button>
        <Footer />
    </div>
}

export default App;