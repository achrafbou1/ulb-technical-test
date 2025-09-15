import {z} from 'zod'

export const NoteSchema = z.object({
  id: z.number(),
  matricule: z.string(),
  mnemonique: z.string(),
  note: z.number()
})

export type Note = z.infer<typeof NoteSchema>

export const NoteArraySchema = z.array(NoteSchema)