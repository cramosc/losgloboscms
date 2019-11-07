function storageAvailable(type) {
    try {
        var storage = window[type],
            x = '__storage_test__';
        storage.setItem(x, x);
        storage.removeItem(x);
        return true;
    }
    catch(e) {
        return e instanceof DOMException && (
                // everything except Firefox
            e.code === 22 ||
            // Firefox
            e.code === 1014 ||
            // test name field too, because code might not be present
            // everything except Firefox
            e.name === 'QuotaExceededError' ||
            // Firefox
            e.name === 'NS_ERROR_DOM_QUOTA_REACHED') &&
            // acknowledge QuotaExceededError only if there's something already stored
            storage.length !== 0;
    }
}

var source   = $("#losglobos-template").html();
var template = Handlebars.compile(source);
var content = $("#content-placeholder");
var localStorage = storageAvailable('localStorage') ? window.localStorage : null;
var currentLanguage = (localStorage && localStorage.getItem('language')) || 'de';

content.html(template(l10n[currentLanguage]));
addListeners();
onLangLoad();

function onLangLoad() {
    makeTablesResponsive();
    resetTarget();
}

function resetTarget() {
    var hash = window.location.hash || '#start';
    hash = hash === '#' ? '#start' : hash;
    window.location.hash = '';
    window.location.hash = hash;
    setTimeout(scrollToTop, 10);
}

function addListeners() {
    var body = $("body");

    body.on("click", ".dropdown-button", function (event) {
        event.stopPropagation();
        $(this).children(".dropdown").toggleClass("active");
    });

    body.on("click", function () {
        $(".dropdown").removeClass("active");
    });

    body.on("click", "#language", function () {
        var delay = $('#container').hasClass("hidden") ? 400 : 0;
        setTimeout(switchLanguage, delay);
    });

    body.on("click", ".navbar-toggle-mobile", function () {
        $(this).next(".header-nav").toggleClass("active");
        $('#container').toggleClass("hidden");
    });

    body.on("click", ".nav-item:not(.dropdown-button), .dropdown-item", function () {
        $(this).closest(".header-nav").removeClass("active");
        $('#container').removeClass("hidden");
    });

    body.on("click", 'a[href^="#"]', function(event) {
        event.preventDefault();
        window.location.hash = this.hash;
        setTimeout(scrollToTop, 10);
    });
}

function switchLanguage() {
    currentLanguage = currentLanguage === 'de' ? 'es' : 'de';
    if (localStorage) {
        localStorage.setItem('language', currentLanguage);
    }
    content.html(template(l10n[currentLanguage]));
    onLangLoad();
}

function scrollToTop() {
    window.scrollTo(0,0);
    $('#content-placeholder').scrollTop(0);
}

function makeTablesResponsive() {
    $('table').wrap('<div style="overflow-x: auto"></div>')
}