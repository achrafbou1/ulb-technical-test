import { z } from 'zod'

export const CoursSchema = z.object({
  mnemonique: z.string(),
  intitule: z.string(),
  credit: z.number(),
  titulaire: z.string()
})

export type Cours = z.infer<typeof CoursSchema>

export const CoursArraySchema = z.array(CoursSchema)