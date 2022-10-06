const tableBody = document.querySelector('tbody')

const loadTable = async () => {
	const request = await fetch('../json/')
	const response = await request.json()
	tableBody.innerHTML = ""
	response.forEach(item => {
		const rowEl = document.createElement('tr')
		const namaBarangEl = document.createElement('td')
		const hargaBarangEl = document.createElement('td')
		const deskripsiEl = document.createElement('td')
		namaBarangEl.textContent = item.fields.nama_barang
		hargaBarangEl.textContent = item.fields.harga_barang
		deskripsiEl.textContent = item.fields.deskripsi
		rowEl.appendChild(namaBarangEl)
		rowEl.appendChild(hargaBarangEl)
		rowEl.appendChild(deskripsiEl)
		tableBody.appendChild(rowEl)
	})
}

const submitEl = document.querySelector("#addModalSubmit")
submitEl.addEventListener("click", async event => {
	event.preventDefault()
	submitEl.disabled = true
	const data = {
		nama_barang: document.querySelector("#namaBarangInput").value,
		harga_barang: document.querySelector("#hargaBarangInput").value,
		deskripsi: document.querySelector("#deskripsiInput").value
	}
	await fetch("submit", {
		method: "POST",
		headers: {
			'Content-Type': 'application/json',
			'X-CSRFToken': window.CSRF_TOKEN
		},
		body: JSON.stringify(data)
	})
	loadTable()
	submitEl.disabled = false
})

loadTable()