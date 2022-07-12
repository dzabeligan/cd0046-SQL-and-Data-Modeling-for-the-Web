const deleteButtons = document.querySelectorAll(".delete-venue");
for (let i = 0; i < deleteButtons.length; i++) {
  const deleteBtn = deleteButtons[i];
  deleteBtn.onclick = function (e) {
    const venueId = e.target.dataset["id"];
    fetch("/venues/" + venueId, {
      method: "DELETE",
    }).then(function () {
      const item = e.target.parentElement;
      item.remove();
    })
  };
}
