// PapaParse CDN loader
(function(){
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/papaparse@5.4.1/papaparse.min.js';
    script.onload = function() {
        window.papaParseLoaded = true;
    };
    document.head.appendChild(script);
})();
