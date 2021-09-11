class MODULE_UL {
    constructor(id) {
        this.ul = document.getElementById(id);
        this.liOne = 0;
    }

    addLink(mat, link) {
        var li = document.createElement("li");
        this.ul.appendChild(li);
        var a = document.createElement("a");
        li.appendChild(a);
        if (link != null && link != 'none') {
            a.href = link;
            a.target = "_blank";
            li.classList.add("matieres");
        } else {
            if (link == 'none') {
                a.classList.add("categorie");
                a.style.fontSize = "16px";
            } else {
                a.classList.add("Ul_titre");
                a.style.fontSize = "20px";
            }
        }
        a.textContent = mat;
        li.id = "li_" + this.liOne;
        this.liOne++;
    }

    sousLink(mat, link) {
        var li = document.getElementById("li_" + (this.liOne - 1));
        var res_li = document.createElement("ol");
        li.appendChild(res_li);
        var a = document.createElement("a");
        res_li.appendChild(a);
        if (link != null) {
            a.href = link;
            a.target = "_blank";
            a.textContent = mat;
            res_li.classList.add("matieres");
        } else {
            a.classList.add("Ul_titre");
            a.textContent = mat;
        }
    }
}

var tAudio = ["Compo.flac"];

function convert(time) {
    var sec = 0;
    var min = 0;
    sec = Math.floor(time);
    min = Math.floor(sec / 60);
    var mins = min >= 10 ? min : '0' + min;
    sec = Math.floor(sec % 60);
    var secs = sec >= 10 ? sec : '0' + sec;
    return mins + ":" + secs;
}