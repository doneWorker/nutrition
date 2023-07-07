import { ref, onMounted, onUnmounted } from "vue";
import { ProductInBasket } from "~/types/products";

const products = ref<ProductInBasket[]>([]);

export function useBasket() {
  const totalSpent = computed(() => {
    return products.value.reduce((total, product) => {
      if (!product.price) return total;

      return total + product.price * product.quantity;
    }, 0);
  });

  const totalMacroNutrients = computed(() => {
    let nutrients = {
      energy: 0,
      protein: 0,
      fat: 0,
      carbs: 0,
    };

    products.value.forEach((product) => {
      if (product.calories) {
        nutrients.energy += Math.round(product.calories * product.quantity);
      }

      if (product.protein) {
        nutrients.protein += Math.round(product.protein * product.quantity);
      }

      if (product.total_fat) {
        nutrients.fat += Math.round(product.total_fat * product.quantity);
      }

      if (product.total_carbohydrates) {
        nutrients.carbs += Math.round(
          product.total_carbohydrates * product.quantity
        );
      }
    });

    return nutrients;
  });

  const addProduct = (product: ProductInBasket, quantity: number = 1) => {
    const isFound = products.value.find((item) => item.id === product.id);

    if (isFound) {
      products.value = products.value.map((item) => {
        if (item.id === product.id) {
          item.quantity += quantity;
        }

        return item;
      });
    } else {
      products.value.push({ ...product, quantity: 1 });
    }
  };

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

  return {
    products,
    totalSpent,
    totalMacroNutrients,
    addProduct,
    removeProduct,
    decreaseQuantity,
    increaseQuantity,
  };
}
