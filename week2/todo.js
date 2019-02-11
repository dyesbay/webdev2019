
let cnt = 1;
function addItem() {
    
    var inputValue = document.getElementById("input").value;
    if(inputValue=== '')
     return;
    var t = document.createTextNode(inputValue) ;

    var section = document.createElement("section");
    section.className="items";
    var input = document.createElement("input");
    input.type="checkbox";
    
    cnt=cnt+1;
    section.id="sec" + cnt;
    input.id="cbx" + cnt;
    section.appendChild(input);
    var label = document.createElement("label");
    label.htmlFor=input.id;
    // input.parentNode.innerText.style.textDecoration="line-through";
    input.onchange = function () {
        if(this.checked)
                this.parentNode.style.textDecoration ="line-through";
        else 
                this.parentNode.style.textDecoration ="none";
        
    }
    label.appendChild(t);
    section.appendChild(label);
    document.getElementById("input").value = "";
    var button = document.createElement("button");
    button.id='btn' + cnt;
    button.type="button";
    button.className='close';
    button.onclick= function (){
        this.parentNode.style.display = 'none';
        // document.getElementById("sec3").deleteItem;
    }
    button.innerText='✖';
    section.appendChild(button);
    document.getElementById("ims").appendChild(section);
}
