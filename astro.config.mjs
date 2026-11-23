import { defineConfig } from 'astro/config';

// Actions supplies the Pages origin and repository path automatically.
export default defineConfig({
  site: process.env.SITE_URL || 'https://Interacti0n.github.io',
  base: process.env.BASE_PATH || '/',
  trailingSlash: 'always',
  output: 'static',
});
