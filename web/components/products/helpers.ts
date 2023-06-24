const MAX_CALORIES = 900;
const MAX_FAT = 100;
const MAX_CARBS = 90;
const MAX_PROTEIN = 80;

type NutrientType = "energy" | "protein" | "fat" | "carbs";

export const getNutritionPercentage = (
  value: number,
  nutrientType: NutrientType
) => {
  let max = 0;
  switch (nutrientType) {
    case "energy":
      max = MAX_CALORIES;
      break;
    case "protein":
      max = MAX_PROTEIN;
      break;
    case "fat":
      max = MAX_FAT;
      break;
    case "carbs":
      max = MAX_CARBS;
      break;
  }

  return Math.round((value / max) * 100);
};
