export type NutrimentItem = { id: string; name: string; value?: number };

export const macroNutriments: NutrimentItem[] = [
  {
    id: "energy",
    name: "Energy",
  },
  {
    id: "protein",
    name: "Protein",
  },
  {
    id: "fat",
    name: "Fat",
  },
  {
    id: "carbs",
    name: "Carbs",
  },
];
