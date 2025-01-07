![[Pasted image 20241015154236.png]]

## Mejoras Posibles

```java
@Service
public class StockService {
    @Autowired
    IProductRepository pR;

    public void checkStock(List<Product> products) {
        for (Product product : products) {
            Product productFullData = pR.findById(product.getId()).orElseThrow();
            if (productFullData.getQtyLeft() < 1) {
                throw new OutOfStockException("No hay stock de: " + productFullData.getName());
            }
        }
    }

    public void updateStock(List<Product> products) {
        for (Product product : products) {
            Product productFullData = pR.findById(product.getId()).orElseThrow();
            productFullData.setQtyLeft(productFullData.getQtyLeft() - 1);
            pR.save(productFullData);
        }
    }
}

@Service
public class SaleService implements ISaleService {
    @Autowired
    ISaleRepository sR;
    @Autowired
    StockService stockService;

    @Override
    public ResponseEntity<Object> createSale(@NotNull Sale sale) {
        try {
            stockService.checkStock(sale.getListProducts());
            stockService.updateStock(sale.getListProducts());
            sR.save(sale);
            // Crear respuesta exitosa...
        } catch (OutOfStockException e) {
            // Manejar excepción y crear respuesta de error...
        }
    }
}



```


## Ejemplo de actualizacion parcial

![[Pasted image 20241017024018.png]]