import React from "react";

function Footer(){
    var date = new Date();
    var currYear = date.getFullYear();
    return <footer>copyrigths {currYear}</footer>
}

export default Footer;