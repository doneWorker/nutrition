export function randomInt(from: number, to: number): number {
  const range = to - from + 1;
  return Math.floor(Math.random() * range) + from;
}
