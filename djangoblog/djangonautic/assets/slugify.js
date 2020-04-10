const title = document.querySelector('input[name=title]');
const slug  = document.querySelector('input[name=slug]');

const slugify = (val) => {
    return val.toString().toLowerCase().trim()
    .replace(/&/g, '-and-')     // replaces & with -and-
    .replace(/[\s\W-]+/g, '-')  // replaces spaces, blanks with -
    .replace(/-$/, '')          // replaces ? or . or ! or anything non-alphabetic at title's end
}

title.addEventListener('keyup', (e) => {
    slug.setAttribute('value', slugify(title.value));
});