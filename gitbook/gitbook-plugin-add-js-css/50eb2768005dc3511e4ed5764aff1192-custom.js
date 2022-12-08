document.onclick = function(e){ 
    if(e.target.tagName === "IMG") {
        window.open(e.target.src, e.target.src);
    }
}
