export type ProductItemModel = {
  id: string;
  name: string;
  price: number;
  image_url: string;
  title: string;
  calories: number;
  protein: number;
  total_fat: number;
  total_carbohydrates: number;
};

export type ProductInBasket = Partial<ProductItemModel> & {
  quantity: number;
};
