export interface FetchProductsPayload {}

export interface ProductResponse {}

export const fetchProducts = async (payload: FetchProductsPayload) => {
  const resp: any = await $fetch("/api/products").catch((error) => error.data);

  return resp.data;
};
