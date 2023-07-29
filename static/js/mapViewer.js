const mapViewerImg = document.getElementById('mapViewerImg');

function getImgUrl(letter) {
    switch(letter){
        case 'A':
            return '/static/img/map01.jpg';
        case 'B':
            return '/static/img/map02.jpg';
        case 'C':
            return '/static/img/map03.jpg';
        case 'D':
            return '/static/img/map04.jpg';
        default:
            return '/static/img/map_default.jpg';
    }
}

function mapViewer(bookcase) {
    const mapUrl = getImgUrl(bookcase);
    mapViewerImg.src = mapUrl;
    mapViewerImg.alt = bookcase + '_Map';
}
