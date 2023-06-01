import jwt_decode, { JwtPayload } from "jwt-decode";

const redirectGuestTo = "/auth/sign-in";

export default defineNuxtRouteMiddleware(() => {
  console.log("onlyusers");
  if (process.client) return;

  const token = useCookie("access_token");
  const parsed: JwtPayload | null = token?.value
    ? jwt_decode(token.value)
    : null;
  console.log("parsed", parsed);
  const tokenExpired = parsed?.exp && parsed.exp < Date.now() / 1000;

  if (parsed === null || tokenExpired) {
    return navigateTo(redirectGuestTo);
  }
});
