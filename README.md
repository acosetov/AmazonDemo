# AmazonDemo

##### Tast:
Write  a crawler that grabs first 3 pages from amazon for selected category:\
https://www.amazon.com/s?i=specialty-aps&bbn=16225011011&rh=n%3A%2116225011011%2Cn%3A10802561&ref=nav_em_T1_0_4_NaN_15__nav_desktop_sa_intl_cleaning_supplies


Result should be save to the file "result.jl"

In the file should be next results:
 - the name of the product
 - url to the product`s picture
 - url to the product`s page (the url should have next format: https://www.amazon.com/Vileda-137578-Supermocio-3xaction-Completo/dp/B005U94MVY/)
 - the price of the product ( the price should have integer type)



As a conclusion json element should like this:
```json
{
    "name": "Vileda Supermocio 3xaction Completo",
    "url": "https://www.amazon.com/Vileda-137578-Supermocio-3xaction-Completo/dp/B005U94MVY/",
    "image_url": "https://m.media-amazon.com/images/I/81G8kuiYh7L._AC_UY218_ML3_.jpg",
    "price": 25.59
}
```