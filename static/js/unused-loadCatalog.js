function displayCatalogs() {
    const loadingIndicator = document.getElementById("loadingIndicator");
    loadingIndicator.style.display = "block";
    const typeToNameMapping = catalogTypeTranslations;
    
    fetch("https://erma.ro/catalog_db-3.7/active_catalogs")
      .then((response) => response.json())
      .then((data) => {
        const productsSection = document.querySelector(".products");
        // Clear existing content
        productsSection.innerHTML = "";

        // Group catalogs by type
        const catalogsByType = data.reduce((acc, catalog) => {
          if (!acc[catalog.type]) {
            acc[catalog.type] = [];
          }
          acc[catalog.type].push(catalog);
          return acc;
        }, {});

        // Create and append sections for each type
        Object.entries(catalogsByType).forEach(([type, catalogs]) => {
          // Use the mapping to get a user-friendly name for the type
          const userFriendlyName = typeToNameMapping[type] || type; // Fallback to type if no mapping exists

          const header = document.createElement("h3");
          header.className = "product-catalog-subheader";
          header.textContent = userFriendlyName;

          // Append header to products section
          productsSection.appendChild(header);

          // Create and append catalogs for this type
          catalogs.forEach((catalog) => {
            const catalogDiv = document.createElement("div");
            catalogDiv.className = "product-catalog";

            
            const catalogLink = document.createElement("a");
            catalogLink.href = catalog.url;

            const catalogImage = document.createElement("img");
            catalogImage.src = catalog.image;
            catalogImage.alt = `Front page of catalog ${catalog.name}`;
            catalogImage.title = catalog.name;
            catalogImage.loading = "lazy";

            const picture = document.createElement("picture");

            // const sourceWebP = document.createElement("source");
            // sourceWebP.srcset = catalog.image.replace(".jpg", ".webp");
            // sourceWebP.type = "image/webp";
            if (catalog.image.startsWith("images/")) {
              const sourceWebP = document.createElement("source");
              // Replace the file extension with .webp
              sourceWebP.srcset = catalog.image
                .replace(".jpg", ".webp")
                .replace(".jpeg", ".webp")
                .replace(".png", ".webp");
              sourceWebP.type = "image/webp";
              picture.appendChild(sourceWebP); // Add WebP source only if condition is met
              picture.appendChild(catalogImage);
            } else {
              catalogLink.appendChild(catalogImage);
            }



            const catalogLinkText = document.createElement("a");
            catalogLinkText.href = catalog.url;
            catalogLink.appendChild(picture);

            const catalogText = document.createElement("div");
            catalogText.className = "product-catalog-text";
            catalogText.innerHTML = catalog.name;

            catalogLinkText.appendChild(catalogText);

            catalogDiv.appendChild(catalogLink);
            catalogDiv.appendChild(catalogLinkText);
            productsSection.appendChild(catalogDiv);
          });
        });
        loadingIndicator.style.display = "none";
      })
      .catch((error) => {
        console.error("Error fetching catalogs:", error);
        loadingIndicator.style.display = "none";
      });
  }

  window.onload = displayCatalogs