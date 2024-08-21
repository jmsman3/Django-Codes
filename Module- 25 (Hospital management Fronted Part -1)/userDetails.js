const loadUserdetails = () => {
  const user_id = localStorage.getItem("user_id");
  // console.log(user_id);
  fetch(`https://testing-8az5.onrender.com/users/${user_id}`)
  
    .then((res) => res.json())
    .then((data) => {
      console.log(data.id);
      const parent = document.getElementById("user-detail-container");
      const div = document.createElement("user-all");
      div.classList.add("user-all");
      div.innerHTML = `
           <div class="user-img">
            <img src="./images/man-1.jpg" alt="">
        </div> 
        <div class="user-info">
            <h1>${data.username}</h1>
            <h3>${data.first_name + data.last_name}</h3>
            <h5>${data.email}</h5>

        </div>
      `;
      parent.appendChild(div);
    });
};
loadUserdetails();
