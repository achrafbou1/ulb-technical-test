import type {ZodSchema} from 'zod'
import {ref} from 'vue'

export function useEntity<T>(endpoint: string, schema: ZodSchema<T[]>) {

    const data = ref<T[]>([])
    const pending = ref(true)
    const error = ref<Error | null>(null)

    const fetchData = async () => {
        pending.value = true
        error.value = null
        try {
            const raw = await $fetch(`/api${endpoint}`)
            data.value = schema.parse(raw)
        } catch (err: unknown) {
            if (err instanceof Error) {
                error.value = err
            } else {
                console.error('Unexpected error:', err)
            }
        } finally {
            pending.value = false
        }
    }

    fetchData()

    return {data, pending, error, refresh: fetchData}
}