import jwt_decode, { JwtPayload } from "jwt-decode";

const redirectUserTo = "/dashboard";

export default defineNuxtRouteMiddleware(() => {
  console.log("process", process);
  if (process.client) return;

  const token = useCookie("access_token");
  const parsed: JwtPayload | null = token?.value
    ? jwt_decode(token.value)
    : null;
  const tokenExpired = parsed?.exp && parsed.exp < Date.now() / 1000;

  if (parsed && !tokenExpired) {
    return navigateTo(redirectUserTo);
  }
});
