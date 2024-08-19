const load_ALL_Products = () => {
    fetch("https://fakestoreapi.com/products")
      .then((res) => res.json())
      .then((data) => Show_All_Products(data))
      .catch((err) => console.log(err));
  };
  
  const Show_All_Products = (products) => {
    const parent = document.getElementById("card-parent");
    parent.innerHTML = "";
    products?.forEach((product) => {
      const div = document.createElement("div");
      div.classList.add("card");
      div.innerHTML = `
          <img class="card-img-top mt-2" src="${product.image}" alt="Card image cap">
          <div class="card-body">
              <h5 class="card-title">${product.title.slice(0, 10)}</h5>
              <p>Price- $${product.price}</p>
              <p class="card-text"><h5>Description</h5>-${product.description.slice(0, 50)}</p>
              <p>Ratings:-${product.rating.rate} Count:-${product.rating.count}</p>
              <a target="_blank" href="ProductDetail.html?ProductId=${product.id}" class="btn btn-primary">Details</a>
               
                <h4>Category:-<a href="#" class="btn btn-warning mt-2">${product.category}</a></h4>
          </div>
      `;
      parent.appendChild(div);
    });
  };
  
  const load_ALL_Categories = () => {
    fetch("https://fakestoreapi.com/products/categories")
      .then((res) => res.json())
      .then((data) => {
        const parent = document.getElementById("drop-deg");
        data.forEach((item) => {
          const li = document.createElement("li");
          li.classList.add("dropdown-item");
          li.innerText = item;
          li.addEventListener("click", () => load_ParticularCategory(item));
          parent.appendChild(li);
        });
      });
  };
  
  const load_ParticularCategory = (category) => {
    fetch(`https://fakestoreapi.com/products/category/${category}`)
      .then((res) => res.json())
      .then((data) => {
        const parent = document.getElementById("card-parent");
        parent.innerHTML = "";
        Show_All_Products(data);
      });
  };
  
 
  load_ALL_Products();
  load_ALL_Categories();
  