// alert('hi');




class MyHeader extends HTMLElement {
    connectedCallback() {
        this.innerHTML = ` 
        <div class="nav_div">
        < nav class="heder_navbar" >


        <ul>
            <li>
                <img src="download.png" alt="Italian Trulli" style="height: 30%; width: 30%;">
            </li>

            <li>
                <div class="heder_dropdown">
                    <button class="heder_dropbtn">Products
                        <i class="fa fa-caret-down"></i>
                    </button>
                    <div class="heder_dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                    </div>
                </div>
            </li>
            <li>
                <div class="heder_dropdown">
                    <button class="heder_dropbtn">Solutions
                        <i class="fa fa-caret-down"></i>
                    </button>
                    <div class="heder_dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                    </div>
                </div>
            </li>
            <li>
                <div class="heder_dropdown">
                    <button class="heder_dropbtn">Pricing

                    </button>
                    <br>
                </div>
            </li>
            <li>
                <div class="heder_dropdown">
                    <button class="heder_dropbtn">Docs
                        <i class="fa fa-caret-down"></i>
                    </button>
                    <div class="heder_dropdown-content">
                        <a href="#">Link 1</a>
                        <a href="#">Link 2</a>
                        <a href="#">Link 3</a>
                    </div>
                </div>
            </li>
            <li>
                <div class="heder_dropdown">
                    <button class="heder_dropbtn">Support

                    </button>
                </div>
            </li>

            <li>
                <div class="heder_dropdown">
                    <button class="heder_dropbtn">Go to console

                    </button>
                </div>
            </li>
            <li>
                <div class="heder_dropdown">
                    <button class="heder_dropbtn">Sign in

                    </button>
                </div>
            </li>


        </ul>
</nav >
</div>`


}
}
coustomElements.define('my-heder',MyHeader)





function search_animal() {
    let input = document.getElementById('searchbar').value
    input = input.toLowerCase();
    let x = document.getElementsByClassName('animals');

    for (i = 0; i < x.length; i++) {
        if (!x[i].innerHTML.toLowerCase().includes(input)) {
            x[i].style.display = "none";
        }
        else {
            x[i].style.display = "list-item";
        }
    }
}

