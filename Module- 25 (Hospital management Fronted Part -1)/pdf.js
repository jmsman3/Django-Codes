const handlePdf = () => {
  const doctor_id = new URLSearchParams(window.location.search).get("doctorId");
  console.log(doctor_id);
  const user_id = localStorage.getItem("user_id");

  console.log(`https://testing-8az5.onrender.com/users/${user_id}`);
  fetch(`https://testing-8az5.onrender.com/doctor/list/${doctor_id}`)
    .then((res) => res.json())
    .then((data) => {
      fetch(
        `https://testing-8az5.onrender.com/patient/list/?user_id=${user_id}`
      )
        .then((res) => res.json())
        .then((pdData) => {
          const newData = [data, pdData];
          console.log(newData);
          const parent = document.getElementById("pdf-container");
          const div = document.createElement("div");

          div.innerHTML = `

         <div class="pd d-flex justify-content-around align-items-center p-5">
            <div class="patient doctor p-5">

                <h1>${newData[1].username}</h1>
                <h1>${newData[1].first_name} ${newData[1].last_name}</h1>
                <h1>${newData[1].email}</h1>

            </div>

            <div class="doctor p-5">'

                <img class="w-25" src=${newData[0].image}/>
                <h2 class="doc-name">n${newData[0].full_name}</h2>
                <h3>Designation: designation</h3>
                <h5>Specialaization: speciaalziotion</h5>
                
            </div>
        </div>

        <input id="pdf-system" class="symtom" type="text" />
        <h1 class="text-center p-2 mt-3">${newData[0].fee} BDT</h1>
        `;

        parent.appendChild(div);
        downloadPdf();
        });
    });
};


const downloadPdf = () => {
    const element = document.getElementById("pdf-container");
  
    // Define the options for html2pdf
    const options = {
      margin: 10,
      filename: "appt.pdf",
      image: { type: "jpeg", quality: 0.98 },
      html2canvas: { scale: 2 },
      jsPDF: { unit: "mm", format: "a4", orientation: "portrait" },
    };
  
    // Use html2pdf to generate and download the PDF
      html2pdf(element, options);
      
  };



handlePdf();
