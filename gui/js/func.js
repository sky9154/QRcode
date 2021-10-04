function goPython() {
    eel.buildQRcode(link.value,image.value,picName.value);
};

document.body.addEventListener("keypress", e => {if (e.key == "Enter") goPython();});