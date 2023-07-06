import { ref, onMounted, onUnmounted } from "vue";
import { ProductInBasket } from "~/types/products";

/* TODO: add computed */
const products = ref<ProductInBasket[]>([]);
const total = ref(0);

export function useBasket() {
  const addProduct = (product: ProductInBasket, quantity: number = 1) =>
    products.value.push({ ...product, quantity });

  const removeProduct = (id: string) =>
    (products.value = products.value.filter((product) => product.id !== id));

  const decreaseQuantity = (targetId: string) => {
    products.value = products.value.map((product) => {
      const { quantity, id } = product;
      const isTarget = targetId === id;

      if (isTarget && quantity > 1) {
        product.quantity--;
      }

      if (isTarget && quantity > 0) {
        removeProduct(id);
      }

      return product;
    });
  };

  const increaseQuantity = (id: string) =>
    (products.value = products.value.map((product) => {
      if (product.id === id) {
        product.quantity++;
      }
      return product;
    }));

  // expose managed state as return value
  return {
    products,
    total,
    addProduct,
    removeProduct,
    decreaseQuantity,
    increaseQuantity,
  };
}
