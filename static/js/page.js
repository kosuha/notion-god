const body = document.body;
const notionDiv = document.getElementById("notion");
const godDiv = document.getElementById("god");

// Nav
let navDiv = document.createElement("div");
navDiv.setAttribute("id", "nav");
let navInnerDiv = document.createElement("div");
navInnerDiv.setAttribute("id", "nav-inner");

// Nav title
let titleDiv = document.createElement("div");
titleDiv.innerHTML = document.querySelector("#notion > div:nth-child(1) > div > div > div:nth-child(2) > div.notion-selectable.notion-text-block > div > div > div").innerHTML;
titleDiv.setAttribute("id", "title");

// Nav links
const linkContainer = document.querySelector("#notion > div:nth-child(2) > div > div > div:nth-child(2)");
let linkDiv = document.createElement("div");
linkDiv.setAttribute("id", "link");
for (let i = 2; i <= linkContainer.childElementCount; i++) {
	selector = "#notion > div:nth-child(2) > div > div > div:nth-child(2) > div:nth-child(" + i + ") > div > div:nth-child(2) > div > div";
	const notionLinkDiv = document.querySelector(selector);
	if (notionLinkDiv.childElementCount) {
		let tempLink = document.createElement("a");
		tempLink.setAttribute("href", notionLinkDiv.children[0].getAttribute("href"));
		tempLink.setAttribute("target", "_blank");
		let tempSpan = document.createElement("span");
		tempSpan.textContent = notionLinkDiv.textContent;
		tempLink.appendChild(tempSpan);
		linkDiv.appendChild(tempLink);
	} else {
		let tempLink = document.createElement("div");
		tempLink.textContent = notionLinkDiv.textContent;	
		linkDiv.appendChild(tempLink);
	}
}

navInnerDiv.appendChild(linkDiv);
navInnerDiv.appendChild(titleDiv);
navDiv.appendChild(navInnerDiv);
godDiv.appendChild(navDiv);

// main text
const mainTextContainer = document.querySelector("#notion > div:nth-child(3) > div > div > div:nth-child(2)");
let mainTextdiv = document.createElement("div");
mainTextdiv.setAttribute("id", "main-text");
let mainTextInnerdiv = document.createElement("div");
mainTextInnerdiv.setAttribute("id", "main-text-inner");
for (let i = 2; i <= mainTextContainer.childElementCount; i++) {
	selector = "#notion > div:nth-child(3) > div > div > div:nth-child(2) > div:nth-child(" + i + ")";
	const paragraphDiv = document.querySelector(selector);
	let tempParagraph = document.createElement("p");
	tempParagraph.innerHTML = paragraphDiv.innerHTML;
	mainTextInnerdiv.appendChild(tempParagraph);
}
mainTextdiv.appendChild(mainTextInnerdiv);
godDiv.appendChild(mainTextdiv);

// main img
const mainImageContainer = document.querySelector("#notion > div:nth-child(4) > div > div > div:nth-child(2)");
let mainImagediv = document.createElement("div");
mainImagediv.setAttribute("id", "main-image");
let mainImageInnerdiv = document.createElement("div");
mainImageInnerdiv.setAttribute("id", "main-image-inner");
for (let i = 2; i <= mainImageContainer.childElementCount; i++) {
	selector = "#notion > div:nth-child(4) > div > div > div:nth-child(2) > div:nth-child(" + i + ") > div > div > div > div > div > div > img"
	const imageTag = document.querySelector(selector);
	let tempImageWraper = document.createElement("div");
	let tempImage = document.createElement("img");
	tempImage.setAttribute("src", imageTag.getAttribute("src"));
	tempImageWraper.appendChild(tempImage);
	mainImageInnerdiv.appendChild(tempImageWraper);
}
mainImagediv.appendChild(mainImageInnerdiv);
godDiv.appendChild(mainImagediv);