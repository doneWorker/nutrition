export default defineNuxtRouteMiddleware((to, from) => {
  const user = useCookie("token");

  console.log("guest middleware", user);

  return;
});
