"use strict";

const main_elem = document.body.querySelector("main");

/**
 * @type {HTMLInputElement | null}
 */
const input_url = main_elem.querySelector("input[type='url']");

if (!input_url) throw new Error("URL input missing!");;


const handle_self_url = () => {
    if (input_url.value === "https://cert-checker-1gbs.onrender.com/") {
        input_url.value = "";
    }
};

const main = () => {
    input_url.addEventListener("input", () => handle_self_url());
}

main();