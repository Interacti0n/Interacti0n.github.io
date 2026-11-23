import type { APIRoute } from 'astro';
import { getCollection } from 'astro:content';
export const GET: APIRoute = async ({ site }) => {
  const base = import.meta.env.BASE_URL;
  const paths = [base, `${base}resume/`, ...(await getCollection('projects')).map(p => `${base}projects/${p.id}/`)];
  const urls = site ? paths.map(path => `<url><loc>${new URL(path, site).href}</loc></url>`).join('') : '';
  return new Response(`<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls}</urlset>`, { headers: { 'Content-Type': 'application/xml' } });
};
