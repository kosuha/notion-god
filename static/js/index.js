const urlInput = document.querySelector("#url-input");
const submitButton = document.querySelector("#submit-button");
const pageUrlWraper = document.querySelector("#page-url-wraper");

submitButton.addEventListener("click", () => {
	for (let i = 0; i < pageUrlWraper.childElementCount; i++) {
		pageUrlWraper.children[i].remove();
	}
	submitButton.disabled = true;
	let loading = document.createElement("div");
	loading.textContent = "배포 중...";
	pageUrlWraper.appendChild(loading);

	const url = './deploy';
	const data = {
		notion_url: urlInput.value
	};

	const param = {
		headers: {
			'content-type': 'application/json, charset=UTF-8',
		},
		body: JSON.stringify(data),
		method: 'POST',
	};

	fetch(url, param)
		.then((data) => {return data.json()})
		.then((res) => {
			loading.remove()
			if (res["status"] == 200) {
				deployedPageUrl = "http://" + window.location.host + "/page?notion_url=" + res["result"];
				let pageUrl = document.createElement("a");
				pageUrl.textContent = "배포한 페이지 열기";
				pageUrl.setAttribute("href", deployedPageUrl);
				pageUrl.setAttribute("target", "_blank");
				pageUrlWraper.appendChild(pageUrl);
			} else {
				let cannotDeploy = document.createElement("div");
				cannotDeploy.textContent = "배포 실패 ㅜㅜ";
				pageUrlWraper.appendChild(cannotDeploy);
			}
			submitButton.disabled = false;
		})
		.catch((error) => console.log(error));
});
