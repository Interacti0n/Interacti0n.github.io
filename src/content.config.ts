import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const projects = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(), subtitle: z.string(), summary: z.string(),
    tags: z.array(z.string()), status: z.string(), order: z.number(),
    repository: z.string().url().optional(),
    release: z.string().url().optional(),
    website: z.string().url().optional(),
    image: z.string().optional(), imageAlt: z.string().optional(), imageCaption: z.string().optional(),
    imageWidth: z.number().int().positive().optional(), imageHeight: z.number().int().positive().optional(),
    featured: z.boolean().default(false),
  }),
});
export const collections = { projects };
