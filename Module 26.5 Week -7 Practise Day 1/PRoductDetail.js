const getparamas = () =>{
     const param = new URLSearchParams(window.location.search).get("ProductId");
    //  console.log(param);
    fetch(`https://fakestoreapi.com/products/${param}`)
    .then((res) => res.json())
    // .then((data) => console.log(data));
    .then((data) => Diplay_Single_Product_Detail(data));

};
getparamas();


  
const Diplay_Single_Product_Detail = (product) => {
    console.log(product);
        const parent = document.getElementById("card-parent-single");
        const div = document.createElement("div");
        div.classList.add("card-single");
        div.innerHTML = `
            <img class="mt-2 detail-image-product" src="${product.image}" alt="Product image">
            <div class="card-body">
             
         <p > <h4>Titile:- ${product.title}</h4></p>

              <p><h4>Price: $${product.price}</h4></p>
              <p class="card-text">
                <h5>Description</h5>
                ${product.description}
              </p>
              <p><h4>Ratings: ${product.rating.rate} | Count: ${product.rating.count}</h4></p>
              <h4>Category:- <a href="#" class="btn btn-warning"> ${product.category}</a> </h4>
             
            </div>
          `;
        parent.appendChild(div);
};
